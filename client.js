const ws = new WebSocket("ws://127.0.0.1:8000/");


function send(){     
        ws.send([document.getElementById("fuck").value,document.getElementById("dick").value])
        //console.log(document.getElementById("fuck").value, document.getElementById("dick").value)
        document.getElementById("fuck").value = '';
        document.getElementById("dick").value = '';
        return false;
    }

    function solve(){     
        ws.send("dick")
        //console.log(document.getElementById("fuck").value, document.getElementById("dick").value)
        // document.getElementById("fuck").value = '';
        // document.getElementById("dick").value = '';
        return false;
    }



ws.onmessage = function (event) {
    const maze = (event.data).split("+");
    //console.log(maze);

    let txt = "";
    maze.forEach(myFunction);
    document.getElementById("demo").innerHTML = txt;

    function myFunction(value, index, array) {
        txt += value.replaceAll(" ", "&nbsp;&nbsp;&nbsp;")+ "<br>"; 
    }
}



