var converter = new showdown.Converter(); // 创建转换器实例-converter
    
var mdcontent = document.getElementById("text").innerText;//.innnertText-获取目标标签的文本内容
var html = converter.makeHtml(mdcontent); //将md翻译成html

    
document.getElementById("aftertranslationtext").innerHTML=(html); //.innnerHTM=（）L-向目标标签写入内容  
