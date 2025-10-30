import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './Home.jsx'
import CRM from './CRM.jsx'
export default function App(){
  return (<BrowserRouter>
    <Routes>
      <Route path="/" element={<Home/>}/>
      <Route path="/crm" element={<CRM/>}/>
    </Routes>
  </BrowserRouter>)
}
