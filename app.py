import streamlit as st
import streamlit.components.v1 as components

st.title("FuturePath AI – Career Advisor")

chatbot_ui = """
<style>

#zoro-button{
position:fixed;
bottom:20px;
right:20px;
width:65px;
height:65px;
border-radius:50%;
background:linear-gradient(135deg,#6a5acd,#00c9ff);
color:white;
font-size:26px;
display:flex;
align-items:center;
justify-content:center;
cursor:pointer;
box-shadow:0px 5px 20px rgba(0,0,0,0.3);
z-index:9999;
}

#chatbox{
position:fixed;
bottom:100px;
right:20px;
width:350px;
height:450px;
background:white;
border-radius:12px;
box-shadow:0 10px 30px rgba(0,0,0,0.3);
display:none;
flex-direction:column;
overflow:hidden;
z-index:9999;
}

#chat-header{
background:#6a5acd;
color:white;
padding:12px;
font-weight:bold;
}

#chat-messages{
flex:1;
padding:10px;
overflow-y:auto;
font-size:14px;
}

#chat-input{
display:flex;
border-top:1px solid #eee;
}

#chat-input input{
flex:1;
border:none;
padding:10px;
}

#chat-input button{
background:#6a5acd;
color:white;
border:none;
padding:10px 15px;
cursor:pointer;
}

</style>

<div id="zoro-button" onclick="toggleChat()">Z</div>

<div id="chatbox">

<div id="chat-header">Zoro AI</div>

<div id="chat-messages"></div>

<div id="chat-input">
<input id="message" placeholder="Ask Zoro anything..." />
<button onclick="sendMessage()">Send</button>
</div>

</div>

<script>

function toggleChat(){
var chat=document.getElementById("chatbox");
chat.style.display=chat.style.display==="flex"?"none":"flex";
}

async function sendMessage(){

let input=document.getElementById("message");
let msg=input.value;

if(!msg) return;

let messages=document.getElementById("chat-messages");

messages.innerHTML+=`<div><b>You:</b> ${msg}</div>`;

input.value="";

let response=await fetch("https://jaswin-123.app.n8n.cloud/webhook/d0b53bd3-d095-4507-a411-49a19c9c595f/chat",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
message:msg
})
});

let data=await response.json();

messages.innerHTML+=`<div><b>Zoro:</b> ${data.reply || JSON.stringify(data)}</div>`;

messages.scrollTop=messages.scrollHeight;

}

</script>
"""

components.html(chatbot_ui, height=0)