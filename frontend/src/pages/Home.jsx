import { Link } from 'react-router-dom'
export default function Home(){
  return (<div style={{padding:20}}><h1>RentMini v2</h1>
    <p>Выберите действие:</p>
    <p><Link to="/crm">Открыть CRM</Link></p>
  </div>)
}
