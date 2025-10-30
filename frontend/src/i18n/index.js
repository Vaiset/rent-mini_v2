export const LOCALES = ['en','ru','uk','ro','de','es','fr','ar','he','pl','cs'];
export const t = (lang, key) => (DICTS[lang] && DICTS[lang][key]) || DICTS.en[key] || key;
export const DICTS = {
  en:{ app:'RentMini', crm:'CRM', contact:'Contact realtor', complaint:'Report', send:'Send', title:'Title', price:'Price', country:'Country', city:'City', language:'Language' },
  ru:{ app:'РентМини', crm:'СРМ', contact:'Связаться', complaint:'Жалоба', send:'Отправить', title:'Заголовок', price:'Цена', country:'Страна', city:'Город', language:'Язык' },
  uk:{ app:'RentMini', crm:'CRM', contact:'Зв’язатись', complaint:'Скарга', send:'Надіслати', title:'Заголовок', price:'Ціна', country:'Країна', city:'Місто', language:'Мова' },
  ro:{ app:'RentMini', crm:'CRM', contact:'Contactează', complaint:'Plângere', send:'Trimite', title:'Titlu', price:'Preț', country:'Țară', city:'Oraș', language:'Limbă' },
  de:{ app:'RentMini', crm:'CRM', contact:'Kontakt', complaint:'Beschwerde', send:'Senden', title:'Titel', price:'Preis', country:'Land', city:'Stadt', language:'Sprache' },
  es:{ app:'RentMini', crm:'CRM', contact:'Contacto', complaint:'Queja', send:'Enviar', title:'Título', price:'Precio', country:'País', city:'Ciudad', language:'Idioma' },
  fr:{ app:'RentMini', crm:'CRM', contact:'Contacter', complaint:'Plainte', send:'Envoyer', title:'Titre', price:'Prix', country:'Pays', city:'Ville', language:'Langue' },
  ar:{ app:'RentMini', crm:'CRM', contact:'اتصال', complaint:'شكوى', send:'إرسال', title:'العنوان', price:'السعر', country:'البلد', city:'المدينة', language:'اللغة' },
  he:{ app:'RentMini', crm:'CRM', contact:'צור קשר', complaint:'תלונה', send:'שלח', title:'כותרת', price:'מחיר', country:'מדינה', city:'עיר', language:'שפה' },
  pl:{ app:'RentMini', crm:'CRM', contact:'Kontakt', complaint:'Skarga', send:'Wyślij', title:'Tytuł', price:'Cena', country:'Kraj', city:'Miasto', language:'Język' },
  cs:{ app:'RentMini', crm:'CRM', contact:'Kontakt', complaint:'Stížnost', send:'Odeslat', title:'Název', price:'Cena', country:'Země', city:'Město', language:'Jazyk' }
};
