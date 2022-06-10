Sim Object with: rainLevel / 100, cloudLevel / 100, randomness, weekend [array]

Weekend object with: dayElement, hourElement, lengthElement, raceElement (if it is a race), startTime (day * 24 + time), finishtime (start + length), startIndex (Math.floor(startTime / 300)), finishIndex (min(Math.ceil(finishTime / 300), weekend.length - 1))

for every session:

        let wetCount = 0;
        for (let j = startIndex; j <= finishIndex; j++) {
            if (weekend[j].rainLevel > 0) wetCount++;
        }
        if (wetCount == 0) statistics.drySessions++;
        else if (wetCount == finishIndex - startIndex + 1) statistics.wetSessions++;
        else statistics.mixedSessions++;

        if (raceElement.checked) {
            hasRaceSessions = true;
            if (wetCount == 0) statistics.dryRaceSessions++;
            else if (wetCount == finishIndex - startIndex + 1) statistics.wetRaceSessions++;
            else statistics.mixedRaceSessions++;
            statistics.racesRun++;
        }
        statistics.sessionsRun++;
    }

______________________________________________________

// find shower length
    let isRaining = false;
    let showerLength = 0;
    let sunshineLength = 0;
    for (let i = 0; i < weekend.length; i++) {
        if (weekend[i].rainLevel > 0) {
            if(!isRaining){
                isRaining = true;
                statistics.sunshineLength.push(sunshineLength * 300);
                sunshineLength = 0;
            }
            showerLength++;
        } else {
            if (isRaining) {
                isRaining = false;
                statistics.showerLength.push(showerLength * 300);
                showerLength = 0;
            }
            sunshineLength++;
        }
    }

  // calc average shower length
    if (statistics.showerLength.length > 0) {
        let sum = 0;
        for (let i = 0; i < statistics.showerLength.length; i++) {
            sum += statistics.showerLength[i];
        }
        statistics.averageShowerLength = sum / statistics.showerLength.length;
    }
    // calc average sunshine length
    if (statistics.sunshineLength.length > 0) {
        let sum = 0;
        for (let i = 0; i < statistics.sunshineLength.length; i++) {
            sum += statistics.sunshineLength[i];
        }
        statistics.averageSunshineLength = sum / statistics.sunshineLength.length;
    }

____________________________

function WeatherSim(rainLevel, cloudLevel, randomness, Temp)

randomness = constrain(randomness, 0, 7) [idk what this does lol]
randomnessFactor = randomness/7

    if (randomness > 0) {
        noisePasses = floor(randomnessFactor * 10) + 4;

noiseCoefficients array

  if (randomness > 0) {
        variance = randomnessFactor * 0.4;
        r = constrain(randNormalDist(0, variance), -2 * variance, 2 * variance);
        noiseCoefficients[0] = r * 0.2;
        for (i = 1; i < noisePasses; i++) {
            r = constrain(randNormalDist(0, variance), -2 * variance, 2 * variance);
            noiseCoefficients[i] = (2.5 / noisePasses) * r;
        }
    }


function randNormalDist(baseValue, variance) {
    do {
        a = Math.random() * 2 - 1;
        b = Math.random() * 2 - 1;
        c = a * a + b * b;
    } while (c > 1);
    aa = Math.sqrt(Math.log(c) * -2 / c) * a;
    return baseValue + variance * aa;
}    



otherCoefficients array
	baseValue = constrain(randNormalDist(0, 1.2), -1.6, 1.6);
    otherCoefficients[0] = randNormalDist(baseValue, 1.3);

baseTemp = ambientTempConfig + 1 - 2 * Math.random() * randomnessFactor;    


    this.calculateWeather = function (weektime) {
        result = {
            noise: 0,
            rainLevel: rainLevelConfig,
            cloudLevel: cloudLevelConfig,
            brightness: 0,
            ambientTemp: 0,
            trackTemp: 0,
        };

        if (noisePasses == 0) {
            //skip rain and cloud calculation
            result.noise = rainLevelConfig;
            result.rainLevel = rainLevelConfig;
            result.clouldLevel = cloudLevelConfig;
        }
        else {
            // calculate noise function
            noise = rainLevelConfig;
            noise += weektime / 86400 * noiseCoefficients[0];
            for (i = 1; i < noisePasses; i++) {
                let s = 0;
                s = sin(weektime * 3.14156 / 86400 + otherCoefficients[0]);
                s = sin((s * 86400 / 3.14156 + weektime) * i * 2 * 3.14156 * 2 / 86400);
                noise += s * noiseCoefficients[i];
            }

            result.noise = noise;

            // cloud level is cloud level config + noise
            cloudLevel = noise + cloudLevelConfig;
            result.cloudLevel = constrain(cloudLevel, 0, 1);

            // rain is only allowed to exist if the cloud level is atleast 0.6
            // if the rain level is zero and the randomness is less than four
            // rain is always zero.
            result.rainLevel = 0;
            if ((rainLevelConfig > 0 || randomness > 3) && result.cloudLevel >= 0.6) {
                rainLevel = (cloudLevel - 0.6) * 1.4875 + 0.15;
                // the rain level can never be bigger than the noise
                // this effectivly limits rain to maximum the configured level.
                rainLevel = constrain(rainLevel, 0, noise);
                result.rainLevel = constrain(rainLevel, 0, 1);
            }
            //TODO:: Add wind calculation   
        }

        // the brightness is a cosine with a period of one day (86400 seconds)
        // and offset by two hours (7200 seconds)
        result.brightness = -0.2 - cos((weektime - 7200) / 86400 * 3.14156 * 2);

        // The hottness factor goes up with increasing temperature.
        // Hottness factor is equal to one then the temperature is 25 degrees.
        let hottnessFactor = baseTemp / 25;


        // The ambient temperature starts as the base temperature.
        // It gets hotter and colder based on the brightness; cloud cover
        // reduces the temperature sing.
        // Rain reduces the temperature. The drop in temperatue
        // is higher on hotter days.
        result.ambientTemp = baseTemp
            + (6 - result.cloudLevel * 3) * result.brightness
            - (result.rainLevel * 4 + result.cloudLevel) * hottnessFactor;

        // Track temperatures goes up with increasing sunlight.
        // At night the track is the same temperature as the air.
        // I dont fully understand this crazy formula.
        let brightnessClipped = max(result.brightness, 0);
        result.trackTemp = result.ambientTemp +
            (result.ambientTemp + 20) * (0.25 - 0.125 * (result.cloudLevel + result.rainLevel) * hottnessFactor) * brightnessClipped;

        return result;
    }
    