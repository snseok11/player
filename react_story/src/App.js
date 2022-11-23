import logo from './logo.svg';
import './App.css';
import {useState} from 'react'; // state 사용할려면 해야함
// const mode = useState('Welcome'); 이러면 ['Welcome', f] 가 되기에
// const [mode, SetMode] = useState('Welcome'); 으로 구성해주자
function Header(props){
  return <header>
    <h1><a href="./">{props.title}</a></h1>
  </header>
}
function Web_list(){
  return <nav><ol>
  <li><a href='/read/1' >html</a></li>
  <li><a href='/read/2' >css </a></li>
  <li><a href='/read/3' >js </a></li>
</ol></nav>
}
function Web_Hello(){
  return <article>
  <h2>Welcome</h2>
  Hello,web
</article>
}
var objecting ={
  "first" : function First(){
    return 0;
  },
  "two" : function Two(){
    return 1;
  },
}

function App() {
  return (
    <div>
      <Header title = "Probs"></Header>
      <Header title ="Probs2"></Header>
      <Header></Header>
      <Web_list></Web_list>
      <Web_Hello></Web_Hello>
    </div>
  );
}

export default App;
