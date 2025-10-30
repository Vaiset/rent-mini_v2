import { useEffect, useState } from 'react'
import { LOCALES, t } from '../i18n/index.js'

export default function CRM(){
  const [items,setItems]=useState([])
  const [lang,setLang]=useState('ru')
  const [country,setCountry]=useState('')
  const [city,setCity]=useState('')
  useEffect(()=>{
    fetch('/api/listings/').then(r=>r.json()).then(setItems)
  },[])
  const filtered = items.filter(i=> (!country||i.country===country) && (!city||i.city===city))
  return (<div style={{padding:20}}><h2>{t(lang,'crm')} · Listings</h2>
    <div style={{display:'flex',gap:8,margin:'10px 0'}}>
      <select value={lang} onChange={e=>setLang(e.target.value)}>{LOCALES.map(l=> <option key={l} value={l}>{l}</option>)}</select>
      <input placeholder={t(lang,'country')} value={country} onChange={e=>setCountry(e.target.value)} />
      <input placeholder={t(lang,'city')} value={city} onChange={e=>setCity(e.target.value)} />
    </div>
    <ul>{filtered.map(i=> <li key={i.id}>
      <b>{i.title}</b> — ${i.price} · {i.country}/{i.city} · {i.locale} 
      {i.image_url && <img src={i.image_url} alt='' width={80} style={{marginLeft:8}}/>}
      <div style={{marginTop:6}}><a href={`https://t.me/${i.contact_telegram?.replace('@','')||''}`} target='_blank'>{t(lang,'contact')}</a></div>
      <details style={{marginTop:6}}><summary>{t(lang,'complaint')}</summary>
        <form onSubmit={async e=>{e.preventDefault(); const text=e.target.text.value; const r=await fetch('/api/complaints/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams({listing_id:i.id,text})}); alert('sent'); e.target.reset();}}><textarea name='text' rows='3' style={{width:'100%'}} placeholder='Describe issue...'></textarea><button type='submit'>{t(lang,'send')}</button></form>
      </details>
    </li>)}</ul>
  </div>)
}
