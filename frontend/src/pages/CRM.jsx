import { useEffect, useState } from 'react'

export default function CRM(){
  const [items,setItems]=useState([])
  useEffect(()=>{
    fetch('/api/listings/').then(r=>r.json()).then(setItems)
  },[])
  return (<div style={{padding:20}}><h2>CRM · Listings</h2>
    <ul>{items.map(i=> <li key={i.id}>{i.title} — ${i.price}</li>)}</ul>
  </div>)
}
