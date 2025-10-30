import { Link } from 'react-router-dom'
import { LOCALES } from '../i18n/index.js'
export default function Home(){
  return (<div style={{padding:20}}><h1>RentMini v2</h1>
    <p><Link to="/crm">Open CRM</Link></p>
  </div>)
}
