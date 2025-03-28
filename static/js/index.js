const userInput = document.getElementById("userInput");
        const outputArea = document.getElementById("outputArea");




        // 确保输入框获得焦点
        userInput.focus();


         // 逐个字符输出
        function typeWriter(elementId, text, speed) {
            let i = 0;
            const element = document.getElementById(elementId);
            
            function typing() {
                if (i < text.length) {
                    element.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(typing, speed);
                }
            }

            typing();
        }

        const text1 = "whatpigeon?-this is“乐鸽”.(index_page)";
        const text2 = "在下方，输入“command”获取可用指令。";
        const text3 = "➜Type:";
        const speed = 50;
        typeWriter('index1', text1, speed); // 第一个标签，每100ms输出一个字符
        setTimeout(() => typeWriter('index2', text2, 100), text1.length * speed); // 第二个标签，延迟输出
        setTimeout(() => typeWriter('index3', text3, 100), (text1.length + text2.length) * speed + 1100); // 第3个标签，延迟输出

        
        


        

        // 监听用户输入
        userInput.addEventListener("keydown", function(event) {
            if (event.key === "Enter") {
                const command = event.target.value.trim();
                processCommand(command);
                event.target.value = ""; // 清空输入框
            }
        });

        // 处理用户输入的命令
        function processCommand(command) {
            let output = "";
            switch (command) {
                case "command":
                    output = `
                    <div id='oop'>
                        
                        <span  class="return">check</span>
                        <br>
                        本站支持的全部命令
                        <br>
                            
                            - 输入 'command' 以获取本站支持的命令。
                           
                            <br>
                            - 输入 'blog' 以获取博客列表。
                            <br>
                            - 输入 'link' 以获取友链列表。
                            <br>
                            - 输入 'about'以获取“关于这里的简单介绍”。
                            <br>
                            - 输入 'exchange' 与本站交换友链。
                             <br>
                            - 输入 'contact' 可联系站长。
                            <br>
                            - 输入 'clear' 可清空输出框。
                            
                    </div>    
                    `
                    ;
                    break;
                /*case "help":
                        output = `
                        <div id='oop'>
                            
                            <span  class="return">check</span>
                            <br>
                            也是返回全部命令
                            - 输入 'command' 以获取本站支持的命令。
                           
                            <br>
                            - 输入 'list' 以获取blog列表。
                            <br>
                            - 输入 'link' 以获取友链。
                             <br>
                            - 输入 'addlink' 以添加友链。
                             <br>
                            - 输入 'contact' 以获取站长联系方式。
                            <br>
                            - 输入 'clear' 以清空输出框。
                             <br>
                           - 输入 'pwd' 以获取当前目录。 
                            <br>
                            - 输入 'ls' 以获取当前目录的文件。

                             <br>
                            - 输入 'about' 以获取本站的跟多信息。
                               <br>
                            - 输入 'help' 也是获取本站可用命令。
                              <br>

                            - 输入 '咕咕咕' 观看大匹咕。
                        </div>    
                        `
                        ;
                    break;
                */
                /*case "pwd":
                    output = `
                   <div id='oop'>
                       
                        <span  class="return">check</span>
                        <br>
                        /什么大匹咕
                    </div>  
                    `
                    ;
                    break;
                */
                /*case "咕咕咕":
                        output = `
                       <div id='oop'>
                           
                            <span  class="return">check</span>
                            <br>
                           <img src="static/image/ggg.jpg" alt="" style="max-width:100%;">
                           <br>
                           咕咕咕，这是ai想象出来的大匹咕。
                        </div>  
                        `
                        ;
                    break;
                */
                case "about":
                        output = `
                       <div id='oop'>
                           
                            <span  class="return">check</span>
                            <br>
                            00后。这是我的博客。关于“关于”就先简单写到这吧。
                            <br>
                            ————另外，欢迎欢迎(￣~▽~￣)ノ...
                            
                            
                    
                        </div>  
                        `
                        ;
                    break;
                case "exchange":
                        output = `
                       <div id='oop'>
                           
                            <span  class="return">check</span>
                            <br>
                            这是本站点的信息交换卡片。  <br>
                            <div style="border-style: solid;padding: 10px;border-width: 1px;border-radius: 6px;">
                                    
                                    博客名称：
                                   
                                    乐鸽.(index_page) <br>
                                    网站地址：
                                   
                                    www.whatpigeon.com <br>
                                    简单介绍：(样式不限，50个字符以内)
                                    <div style="max-width:100% ;word-break: break-all;padding-left: 85px;">
                                        
                                          路灯下我的身影，是最短的距离。
                                    </div>
                                    
                                    头像地址：(也可以直接发送图片)
                                    <div style="max-width:100% ;word-break: break-all;padding-left: 85px;">
                                        http://whatai.online/myfirtpixelpicture.png
                                    </div>
                                     
                                    
                                    
                            </div>
                            请将站点信息发送到我的邮箱。<br>
                            可输入"contact"返回联系方式。
                        </div>  
                        `
                        ;
                    break;
                case "contact":
                        output = `
                       <div id='oop'>
                           
                            <span  class="return">check</span>
                           <br>
                            站长联系方式。
                            <br>
                            1.邮箱：whatpigeon66@gmail.

                        `
                        ;
                    break;
                /*case "ls":
                    output = `
                   <div id='oop'>
                       
                        <span  class="return">check</span>
                        <br>
                        是空目录，以下是一些本站支持的命令。
                        <br>
                        - 输入 'list' 以获取blog列表。
                        <br>
                        - 输入 'link' 以获取友链。
                         <br>
                        - 输入 'addlink' 去互换友链。
                        <br>
                        - 输入 'clear' 以清空输出框。
                    </div>    
                    
                    `
                    ;
                    break;
                    */
                case "blog":
                    var two = document.getElementById("one").innerHTML;
                    output = ` 
                 
                    <div id='oop'>
                        
                        <span  class="return">check</span>
                        <br>
                        ${two}
                    </div>    

                    `;
                    break;
                case "link":
                    var three = document.getElementById("two").innerHTML;
                    output = ` 
                   <br>
                   <div id='oop'>
                        
                        <span  class="return">check</span>
                        <br>
                        ${three} 
                    </div>    
                    
                     
                    `;
                    break;
                
               
                case "clear":
                    outputArea.innerHTML = ""; // 清空终端输出
                    createNewInputLine(); // 重新创建输入框
                    return; // 不创建命令输出
                default:
                    output = ` 
                    <br>
                        <span  class="erro">erro-1</span> 
                        <br>
                        '${command}'
                        <span id='ii'> 
                        不是内部或外部命令，也不是可执行的程序或批处理文件。
                        </span>
                    `;
                    break;
            }

            // 显示命令输出
            const newOutput = document.createElement("div");
            newOutput.innerHTML = ` <br> <span  class="get-input">Typein</span> '${command}'\n${output}`;
            outputArea.appendChild(newOutput);

            // 删除原来的输入框
            const currentInputLine = document.querySelector(".input-line");
            currentInputLine.remove();

            // 创建新的输入框行并绑定事件
            createNewInputLine();
        }

        // 创建新的输入框行并绑定事件
        function createNewInputLine() {
            // 创建新的输入框行
            const newInputLine = document.createElement("div");
            newInputLine.classList.add("input-line");
            newInputLine.innerHTML = `<span class="prompt" id="prompt">➜<b>Type:</b></span><input type="text" id='userInput'  autofocus>`;
            outputArea.appendChild(newInputLine);

            // 为新输入框绑定键盘事件
            const newInput = newInputLine.querySelector("input");
            newInput.addEventListener("keydown", function(event) {
                if (event.key === "Enter") {
                    const command = event.target.value.trim();
                    processCommand(command);
                    event.target.value = ""; // 清空输入框
                }
            });

            // 聚焦新输入框
            newInput.focus();

            // 自动滚动到底部
            outputArea.scrollTop = outputArea.scrollHeight;
        }