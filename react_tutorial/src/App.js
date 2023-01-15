
import './App.css';
import { useState } from 'react';

function Headers(props){
  const lis = [
  ]
  for(let i = 0; i<props.topics.length; i++) {
    let t = props.topics[i];
    lis.push(<li key={t.id}><a id = {t.id} href = {'/read/'+t.id} onClick={(event)=>{
      event.preventDefault();
      props.onChangeMode2(event.target.id);
    }}>{t.title}</a></li>)
  }
  return (<header className="App-header">
  <h1><a href="#" onClick={(event)=>{
      event.preventDefault();
      props.onChangeMode();
    }}>WEB</a></h1>
  {lis}
</header>)
}
function Nav_Art(props){
  return (<p><h2>{props.title}</h2>
  {props.body}</p>)
}

function App() {
  // const _mode = useState('Welcome');
  // const mode = _mode[0];
  // const setMode = _mode[1];
  const [mode, setMode] = useState('Welcome');
  const [id , setid] = useState(null)
  const topics = [
    {id:1, title:'html', body:'html is ...'},
    {id:2, title:'css', body:'css is ...'},
    {id:3, title:'js', body:'js is ...'},
  ];
  let content = null;
  if(mode === 'Welcome'){
    content = <Nav_Art title = "Welcome to React" body="Hello, Web!"></Nav_Art>
  }
  else if(mode === 'read'){
    content = <Nav_Art title = "Welcome to read" body="Hello, read!"></Nav_Art>
  }
  return (
    <div className="App">
      <Headers topics = {topics} onChangeMode={()=>{
        setMode('read')
      }} onChangeMode2={(id)=>{
        alert(id)
      }}></Headers>
      {content}
    </div>
  );
}

export default App;
