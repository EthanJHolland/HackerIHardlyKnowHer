//based on tutorial at https://9to5google.com/2015/06/14/how-to-make-a-chrome-extensions/

var elements = document.getElementsByTagName('*');
var replacedText;
var text;
for (var i = 0; i < elements.length; i++) {
    var element = elements[i];

    for (var j = 0; j < element.childNodes.length; j++) {
        var node = element.childNodes[j];

        if (node.nodeType === 3) {
            // var replacedText = text.replace(/[word or phrase to replace here]/gi, '[new word or phrase]');
            text=node.nodeValue;
            replacedText=transform(text);

            if (replacedText !== text) {
                element.replaceChild(document.createTextNode(replacedText), node);
            }
        }
    }
}

function transform(text){
    var words = text.split(" ");
    var out = "";
    var added;
    for (var i = 0; i < words.length; i ++) {
        added="";
        if(words[i].endsWith('er') || words[i].endsWith('or')){
            if(isVerb(words[i].substring(0, words[i].length-2))){
                added=" ("+words[i]+" her? I hardly know her!)";
            }
        }
        out+=words[i]+added+" ";
    }
    return out;
}

function isVerb(word){
    return false;
}