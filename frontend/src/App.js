import logo from './logo.svg';
import './App.css';
import Graph from "./components/graph";
import "@progress/kendo-theme-material/dist/all.css";
import "hammerjs";
import {FlavorForm, Line} from './components/line'


function App() {
   return (
 <div className="App">
 <div className="container">
 {/* other graphs */}
 <div className="section">
  <div className="react-form">
   <FlavorForm/>
  </div>
 <Line />
 </div>
 </div>
 </div>
  );
}

export default App;
