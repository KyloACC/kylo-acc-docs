import mmap
import struct
import copy
import os
from enum import Enum
import math



class ACC_STATUS(Enum):

    ACC_OFF = 0
    ACC_REPLAY = 1
    ACC_LIVE = 2
    ACC_PAUSE = 3


class ACC_SESSION_TYPE(Enum):

    ACC_UNKNOW = -1
    ACC_PRACTICE = 0
    ACC_QUALIFY = 1
    ACC_RACE = 2
    ACC_HOTLAP = 3
    ACC_TIME_ATTACK = 4
    ACC_DRIFT = 5
    ACC_DRAG = 6
    ACC_HOTSTINT = 7
    ACC_HOTLAPSUPERPOLE = 8


class ACC_FLAG_TYPE(Enum):

    ACC_NO_FLAG = 0
    ACC_BLUE_FLAG = 1
    ACC_YELLOW_FLAG = 2
    ACC_BLACK_FLAG = 3
    ACC_WHITE_FLAG = 4
    ACC_CHECKERED_FLAG = 5
    ACC_PENALTY_FLAG = 6
    ACC_GREEN_FLAG = 7
    ACC_ORANGE_FLAG = 8


class ACC_PENALTY_TYPE(Enum):
    No_penalty = 0
    DriveThrough_Cutting = 1
    StopAndGo_10_Cutting = 2
    StopAndGo_20_Cutting = 3
    StopAndGo_30_Cutting = 4
    Disqualified_Cutting = 5
    RemoveBestLaptime_Cutting = 6

    DriveThrough_PitSpeeding = 7
    StopAndGo_10_PitSpeeding = 8
    StopAndGo_20_PitSpeeding = 9
    StopAndGo_30_PitSpeeding = 10
    Disqualified_PitSpeeding = 11
    RemoveBestLaptime_PitSpeeding = 12

    Disqualified_IgnoredMandatoryPit = 13

    PostRaceTime = 14
    Disqualified_Trolling = 15
    Disqualified_PitEntry = 16
    Disqualified_PitExit = 17
    Disqualified_WrongWay = 18

    DriveThrough_IgnoredDriverStint = 19
    Disqualified_IgnoredDriverStint = 20

    Disqualified_ExceededDriverStintLimit = 21


class ACC_TRACK_GRIP_STATUS(Enum):

    ACC_GREEN = 0
    ACC_FAST = 1
    ACC_OPTIMUM = 2
    ACC_GREASY = 3
    ACC_DAMP = 4
    ACC_WET = 5
    ACC_FLOODED = 6


class ACC_RAIN_INTENSITY(Enum):

    ACC_NO_RAIN = 0
    ACC_DRIZZLE = 1
    ACC_LIGHT_RAIN = 2
    ACC_MEDIUM_RAIN = 3
    ACC_HEAVY_RAIN = 4
    ACC_THUNDERSTORM = 5


class accSM(mmap.mmap):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

    def unpack_value(self, value_type: str, padding=0) -> float:
        return struct.unpack(f"={value_type}{padding}x", self.read(4 + padding))[0]

    def unpack_array(self, value_type: str, count: int, padding=0) -> tuple:

        if value_type in ("i", "f"):
            value = struct.unpack(
                f"={count}{value_type}{padding}x", self.read(4 * count + padding))

        else:
            value = self.read(2 * count + padding)

        return value

    def unpack_array2D(self, value_type: str, count: int, subCount: int) -> tuple:
        data = []
        for _ in range(count):
            data.append(self.unpack_array(value_type, subCount))
        return tuple(data)


def bytesTupleToStr(byte: bytes) -> str:
    return byte.decode("utf-16", errors="ignore")


def read_shared_memory(physicSM: accSM, graphicSM: accSM):

    data = []
    lap = 0
    fuelStartLap = 0
    fuelUsedThisLap = 0
    last5Laps = []
    fTyrePressureFL = 0.0
    fTyrePressureFR = 0.0
    fTyrePressureRL = 0.0
    fTyrePressureRR = 0.0
    iTyrePressureCount = 1

    while(True):
        newData = False
        pPacketID = physicSM.unpack_value("i")
        gPacketID = graphicSM.unpack_value("i")
        if len(data) == 0 or pPacketID != data[-1]["physics"]["packetID"]:
            newData = True
            physics = {
                "packetID": pPacketID,

                "gas": physicSM.unpack_value("f"),
                "brake": physicSM.unpack_value("f"),
                "fuel": physicSM.unpack_value("f"),
                "gear": physicSM.unpack_value("i"),
                "rpm": physicSM.unpack_value("i"),
                "steerAngle": physicSM.unpack_value("f"),

                "speedKmh": physicSM.unpack_value("f"),
                "velocity": physicSM.unpack_array("f", 3),
                "accG": physicSM.unpack_array("f", 3),

                "wheelSlip": physicSM.unpack_array("f", 4),
                # Field is not used by ACC
                "wheelLoad": physicSM.unpack_array("f", 4),
                "wheelsPressure": physicSM.unpack_array("f", 4),
                "wheelAngularSpeed": physicSM.unpack_array("f", 4),
                # Field is not used by ACC
                "tyreWear": physicSM.unpack_array("f", 4),
                # Field is not used by ACC
                "tyreDirtyLevel": physicSM.unpack_array("f", 4),
                "tyreCoreTemperature": physicSM.unpack_array("f", 4),
                # Field is not used by ACC
                "camberRAD": physicSM.unpack_array("f", 4),
                "suspensionTravel": physicSM.unpack_array("f", 4),

                # Field is not used by ACC
                "drs": physicSM.unpack_value("i"),
                "tc": physicSM.unpack_value("f"),
                "headeing": physicSM.unpack_value("f"),
                "pitch": physicSM.unpack_value("f"),
                "roll": physicSM.unpack_value("f"),
                # Field is not used by ACC
                "cgHeight": physicSM.unpack_value("f"),
                "carDamage": physicSM.unpack_array("f", 5),
                # Field is not used by ACC
                "numberOfTyresOut": physicSM.unpack_value("i"),
                "pitLimiterOn": physicSM.unpack_value("i"),
                "abs": physicSM.unpack_value("f"),

                # Field is not used by ACC
                "kersCharge": physicSM.unpack_value("f"),
                # Field is not used by ACC
                "kersInput": physicSM.unpack_value("f"),

                "autoshifterOn": physicSM.unpack_value("i"),
                # Field is not used by ACC
                "rideHeight": physicSM.unpack_array("f", 2),
                "turboBoost": physicSM.unpack_value("f"),
                # Not implemented in ACC
                "ballast": physicSM.unpack_value("f"),
                # Field is not used by ACC
                "airDensity": physicSM.unpack_value("f"),
                "airTemp": physicSM.unpack_value("f"),
                "roadTemp": physicSM.unpack_value("f"),
                "localAngularVel": physicSM.unpack_array("f", 3),
                "FinalFF": physicSM.unpack_value("f"),
                # Field is not used by ACC
                "performanceMeter": physicSM.unpack_value("f"),

                # Field is not used by ACC
                "engineBrake": physicSM.unpack_value("i"),
                # Field is not used by ACC
                "ersRecoveryLevel": physicSM.unpack_value("i"),
                # Field is not used by ACC
                "ersPowerLevel": physicSM.unpack_value("i"),
                # Field is not used by ACC
                "ersHeatCharging": physicSM.unpack_value("i"),
                # Field is not used by ACC
                "ersIsCharging": physicSM.unpack_value("i"),
                # Field is not used by ACC
                "kersCurrentKJ": physicSM.unpack_value("f"),

                # Field is not used by ACC
                "drsAvailable": physicSM.unpack_value("i"),
                # Field is not used by ACC
                "drsEnabled": physicSM.unpack_value("i"),

                "brakeTemp": physicSM.unpack_array("f", 4),
                "clutch": physicSM.unpack_value("f"),

                # Field is not used by ACC
                "tyreTempI": physicSM.unpack_array("f", 4),
                # Field is not used by ACC
                "tyreTempM": physicSM.unpack_array("f", 4),
                # Field is not used by ACC
                "tyreTempO": physicSM.unpack_array("f", 4),

                "isAIControlled": physicSM.unpack_value("i"),

                "tyreContactPoint": physicSM.unpack_array2D("f", 4, 3),
                "tyreContactNormal": physicSM.unpack_array2D("f", 4, 3),
                "tyreContactHeading": physicSM.unpack_array2D("f", 4, 3),

                "brakeBias": physicSM.unpack_value("f"),

                "localVelocity": physicSM.unpack_array("f", 3),

                # Field is not used by ACC
                "P2PActivation": physicSM.unpack_value("i"),
                # Field is not used by ACC
                "P2PStatus ": physicSM.unpack_value("i"),

                # Field is not used by ACC
                "currentMaxRpm": physicSM.unpack_value("i"),

                # Field is not used by ACC
                "mz": physicSM.unpack_array("f", 4),
                # Field is not used by ACC
                "fz": physicSM.unpack_array("f", 4),
                # Field is not used by ACC
                "my": physicSM.unpack_array("f", 4),
                "slipRatio": physicSM.unpack_array("f", 4),
                "slipAngle": physicSM.unpack_array("f", 4),

                # Field is not used by ACC
                "tcinAction": physicSM.unpack_value("i"),
                # Field is not used by ACC
                "absinAction": physicSM.unpack_value("i"),
                # Field is not used by ACC
                "suspensionDamage": physicSM.unpack_array("f", 4),
                # Field is not used by ACC
                "tyreTemp": physicSM.unpack_array("f", 4),
                "waterTemp": physicSM.unpack_value("f"),

                "brakePressure": physicSM.unpack_array("f", 4),
                "frontBrakeCompound": physicSM.unpack_value("i"),
                "rearBrakeCompound": physicSM.unpack_value("i"),
                "padLife": physicSM.unpack_array("f", 4),
                "discLife": physicSM.unpack_array("f", 4),

                "ignitionOn": physicSM.unpack_value("i"),
                "starterEngineOn": physicSM.unpack_value("i"),
                "isEngineRunning": physicSM.unpack_value("i"),

                "kerbVibration": physicSM.unpack_value("f"),
                "slipVibrations": physicSM.unpack_value("f"),
                "gVibrations": physicSM.unpack_value("f"),
                "absVibrations": physicSM.unpack_value("f"),
            }

        if len(data) == 0 or gPacketID != data[-1]["graphics"]["packetID"]:

            graphics = {
                "packetID": gPacketID,
                "ac_status": ACC_STATUS(graphicSM.unpack_value("i")),
                "ac_session_type": ACC_SESSION_TYPE(graphicSM.unpack_value("i")),
                "currentTime": bytesTupleToStr(graphicSM.unpack_array("c", 15)),
                "lastTime": bytesTupleToStr(graphicSM.unpack_array("c", 15)),
                "bestTime": bytesTupleToStr(graphicSM.unpack_array("c", 15)),
                "split": bytesTupleToStr(graphicSM.unpack_array("c", 15)),
                "completedLaps": graphicSM.unpack_value("i"),
                "position": graphicSM.unpack_value("i"),
                "iCurrentTime": graphicSM.unpack_value("i"),
                "iLastTime": graphicSM.unpack_value("i"),
                "iBestTime": graphicSM.unpack_value("i"),
                "sessionTimeLeft": graphicSM.unpack_value("f"),
                "distanceTraveled": graphicSM.unpack_value("f"),
                "isInPit": graphicSM.unpack_value("i"),
                "currentSectorIndex": graphicSM.unpack_value("i"),
                "lastSectorTime": graphicSM.unpack_value("i"),
                "numberOfLaps": graphicSM.unpack_value("i"),
                "tyreCompound": bytesTupleToStr(graphicSM.unpack_array("c", 33, 2)),
                # Field is not used by ACC
                "replayTimeMultiplier": graphicSM.unpack_value("f"),
                "normalizedCarPosition": graphicSM.unpack_value("f"),

                "activeCars": graphicSM.unpack_value("i"),
                "carCoordinates": graphicSM.unpack_array2D("f", 60, 3),
                "carID": graphicSM.unpack_array("i", 60),
                "playerCarID": graphicSM.unpack_value("i"),
                "penaltyTime": graphicSM.unpack_value("f"),
                "flag": ACC_FLAG_TYPE(graphicSM.unpack_value("i")),
                "penalty": ACC_PENALTY_TYPE(graphicSM.unpack_value("i")),
                "idealLineOn": graphicSM.unpack_value("i"),
                "isInPitLane": graphicSM.unpack_value("i"),
                # Return always 0
                "surfaceGrip": graphicSM.unpack_value("f"),
                "mandatoryPitDone": graphicSM.unpack_value("i"),
                "windSpeed": graphicSM.unpack_value("f"),
                "windDirection": graphicSM.unpack_value("f"),
                "isSetupMenuVisible": graphicSM.unpack_value("i"),
                "mainDisplayIndex": graphicSM.unpack_value("i"),
                "secondaryDisplyIndex": graphicSM.unpack_value("i"),
                "TC": graphicSM.unpack_value("i"),
                "TCCUT": graphicSM.unpack_value("i"),
                "EngineMap": graphicSM.unpack_value("i"),
                "ABS": graphicSM.unpack_value("i"),
                "fuelXLap": graphicSM.unpack_value("f"),
                "rainLights": graphicSM.unpack_value("i"),
                "flashingLights": graphicSM.unpack_value("i"),
                "lightStage": graphicSM.unpack_value("i"),
                "exhaustTemperature": graphicSM.unpack_value("f"),
                "wiperStage": graphicSM.unpack_value("i"),
                "driverStintTotalTimeLeft": graphicSM.unpack_value("i"),
                "driverStintTimeLeft": graphicSM.unpack_value("i"),
                "rainTyres": graphicSM.unpack_value("i"),
                "sessionIndex": graphicSM.unpack_value("i"),
                "usedFuel": graphicSM.unpack_value("f"),
                "deltaLapTime": bytesTupleToStr(graphicSM.unpack_array("c", 15, 2)),
                "ideltaLapTime": graphicSM.unpack_value("i"),
                "estimatedLapTime": bytesTupleToStr(graphicSM.unpack_array("c", 15, 2)),
                "iestimatedLapTime": graphicSM.unpack_value("i"),
                "isDeltaPositive": graphicSM.unpack_value("i"),
                "iSplit": graphicSM.unpack_value("i"),
                "isValidLap": graphicSM.unpack_value("i"),
                "fuelEstimatedLaps": graphicSM.unpack_value("f"),
                "trackStatus": bytesTupleToStr(graphicSM.unpack_array("c", 33, 2)),
                "missingMandatoryPits": graphicSM.unpack_value("i"),
                "Clock": graphicSM.unpack_value("f"),
                "directionLightsLeft": graphicSM.unpack_value("i"),
                "directionLightsRight": graphicSM.unpack_value("i"),
                "GlobalYellow": graphicSM.unpack_value("i"),
                "GlobalYellow1": graphicSM.unpack_value("i"),
                "GlobalYellow2": graphicSM.unpack_value("i"),
                "GlobalYellow3": graphicSM.unpack_value("i"),
                "GlobalWhite": graphicSM.unpack_value("i"),
                "GlobalGreen": graphicSM.unpack_value("i"),
                "GlobalChequered": graphicSM.unpack_value("i"),
                "GlobalRed": graphicSM.unpack_value("i"),
                "mfdTyreSet": graphicSM.unpack_value("i"),
                "mfdFuelToAdd": graphicSM.unpack_value("f"),
                "mfdTyrePressureLF": graphicSM.unpack_value("f"),
                "mfdTyrePressureRF": graphicSM.unpack_value("f"),
                "mfdTyrePressureLR": graphicSM.unpack_value("f"),
                "mfdTyrePressureRR": graphicSM.unpack_value("f"),
                "trackGripStatus": ACC_TRACK_GRIP_STATUS(graphicSM.unpack_value("i")),
                "rainIntensity": ACC_RAIN_INTENSITY(graphicSM.unpack_value("i")),
                "rainIntensityIn10min": ACC_RAIN_INTENSITY(graphicSM.unpack_value("i")),
                "rainIntensityIn30min": ACC_RAIN_INTENSITY(graphicSM.unpack_value("i")),
                "currentTyreSet": graphicSM.unpack_value("i"),
                "strategyTyreSet": graphicSM.unpack_value("i")
            }

        if newData:
            data.append(copy.deepcopy(
                {"physics": physics, "graphics": graphics}))

        # +- every 0.5s (333Hz)
        if (pPacketID % 166 == 0 and pPacketID != 0):
            test = 0

            if lap != graphics["completedLaps"]:
                test = 1

                last_lap = graphics['iLastTime']
                iMinutes = math.floor(last_lap / 60000)
                sMinutes = f"0{iMinutes}"

                last_lap = last_lap - iMinutes*60000
                iSeconds = math.floor(last_lap / 1000)
                if iSeconds < 10:
                    sSeconds = f"0{iSeconds}"
                else:
                    sSeconds = f"{iSeconds}"

                temp = str(graphics['iLastTime'])
                temp2 = len(temp)-3
                sms = temp[temp2:]
                ims = int(sms) 

                lap = graphics["completedLaps"]
                if fuelStartLap != 0:
                    fuelUsedThisLap = fuelStartLap - physics["fuel"]
                    last5Laps.append(fuelUsedThisLap)

                if len(last5Laps) > 5:
                    last5Laps.pop(0)

                fuelStartLap = physics["fuel"]

                fTyrePressureFL_temp = math.floor((fTyrePressureFL*100)/iTyrePressureCount) / 100
                fTyrePressureFR_temp = math.floor((fTyrePressureFR*100)/iTyrePressureCount) / 100
                fTyrePressureRL_temp = math.floor((fTyrePressureRL*100)/iTyrePressureCount) / 100
                fTyrePressureRR_temp = math.floor((fTyrePressureRR*100)/iTyrePressureCount) / 100


                fTyrePressureFL = 0
                fTyrePressureFR = 0
                fTyrePressureRL = 0
                fTyrePressureRR = 0

            avgFuel5Laps = -1
            if len(last5Laps) == 5:
                avgFuel5Laps = sum(last5Laps) / 5

            fTyrePressureFL = fTyrePressureFL + physics['wheelsPressure'][0]
            fTyrePressureFR = fTyrePressureFR + physics['wheelsPressure'][1]
            fTyrePressureRL = fTyrePressureRL + physics['wheelsPressure'][2]
            fTyrePressureRR = fTyrePressureRR + physics['wheelsPressure'][3]
            iTyrePressureCount += 1

            os.system("cls")
            print(
                f"ID: {pPacketID}\nLap: {lap}\nFuel: {physics['fuel']:.3f}\nFuelThisLap: {fuelUsedThisLap:.3f}\n5 Laps avg: {avgFuel5Laps:.3f}")
            print("Breakdown of the 5 laps average...")
            for i, lapConso in enumerate(last5Laps):
                print(f"Lap {i}: {lapConso:.3f}")

            if test == 1:
                with open("fuel.txt", "a") as f:
                  f.write(f"L: {lap} --- Fuel: {physics['fuel']:.3f} --- Fuel this Lap: {fuelUsedThisLap:.3f} --- Laptime: {sMinutes}:{sSeconds}.{sms}\n")
                with open("tyres.txt", "a") as f:
                  f.write(f"L: {lap} --- {fTyrePressureFL_temp}-{fTyrePressureFR_temp}-{fTyrePressureRL_temp}-{fTyrePressureRR_temp} \n")


                



        physicSM.seek(0)
        graphicSM.seek(0)


def main():

    with accSM(-1, 804, tagname="Local\\acpmf_physics", access=mmap.ACCESS_READ) as physicSM, accSM(-1, 1580, tagname="Local\\acpmf_graphics", access=mmap.ACCESS_READ) as graphicSM:

        if sum(physicSM.read()) != 0:
            # Still pass if acc created the memory map first and is now closed but it's fine in this case.
            physicSM.seek(0)
            print("Reading ACC Shared Memory...")
            read_shared_memory(physicSM, graphicSM)

        else:
            print("ACC isn't running, exiting...")


if __name__ == "__main__":
    main()
