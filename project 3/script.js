function analyzeText(){
    let areaAnalyze = document.getElementById("text");
    let value = areaAnalyze.value;
    let textAnalyze = value.split(/\s+/);

    for(var i = 0; i < textAnalyze.length; i++){
        textAnalyze[i] = textAnalyze[i].trim();
    }

    console.log(textAnalyze);

    const wordChange = document.getElementById("count");
    wordChange.textContent = wordCount(textAnalyze);

    const uniqueChange = document.getElementById("unique");
    uniqueChange.textContent = uniqueWordCount(textAnalyze);

    const sentenceChange = document.getElementById("sentences");
    sentenceChange.textContent = sentenceCount(textAnalyze);

    const numberChange = document.getElementById("number");
    numberChange.textContent = numberCount(textAnalyze);

    const freqChange = document.getElementById("freq");
    freqChange.textContent = mostFrequentWord(textAnalyze);

    return false;
}

function wordCount(array){
    let total = 0;

    for(var i = 0; i < array.length; i++){
        if(array[i]){
            total += 1;
        }
    }
    return total;
}

function uniqueWordCount(array){
    let count = 0;

    for(var i = 0; i < array.length; i++){
        if(!isNaN(array[i])){
            continue;
        }else if(array[i].length < 3){
            continue;
        }
        count += 1;
    }
    return count;
}

function sentenceCount(array){
    count = 0;

    for(var i = 0; i < array.length; i++){
        var varLength = array[i].length;
        if(array[i].charAt(varLength - 1) != '.'){
            continue;
        }
        count += 1;
    }

    return count;
}

function numberCount(array){
    let count = 0;
    
    for(var i = 0; i < array.length; i++){
        if(isNaN(array[i]) || !array[i]){
            continue;
        }
        count += 1;
        console.log(array[i]);
    }
    return count;
}

function mostFrequentWord(array){
    words = {};

    for(var i = 0; i < array.length; i++){
        var word = array[i].toLowerCase();

        if(word in words){
            words[word] += 1;
        }else {
            words[word] = 1;
        }
    }

    var max = 0;
    var maxWord = "";
    
    for(var word in words){
        if(words[word] > max){
            max = words[word];
            maxWord = word;
        }
    }

    return maxWord + " - " + max;
}