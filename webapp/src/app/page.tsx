'use client';

import { FormEvent, useState } from "react"
import toast, { Toaster } from "react-hot-toast"

export default function Home() {
  const [preferences, setPreferences] = useState({});

  return (
    <div className="flex w-full h-full bg-white flex-col justify-start gap-10 text-black">
      <Toaster position="top-right" />
      <h1 className="block ml-auto mr-auto mt-10 text-2xl text-black">Roommate Matching</h1>
      <form className="ml-[10%] mr-[10%] flex flex-col gap-4" onSubmit={(e) => onSubmit(e, preferences)}>
        <div className="flex flex-col width-full justify-between gap-4 md:flex-row">
          <Input placeholder="Name" name="name" input={preferences} setInput={setPreferences} />
          <Input placeholder="Email address" name="email" input={preferences} setInput={setPreferences} />
        </div>
        <div className="flex flex-col width-full justify-between gap-4 md:flex-row">
          <Select placeholder="What time do you usually sleep?" options={{"8-10": "8:00 PM - 10:00 PM", "10-12": "10:00 PM - 12:00 AM", "12-2": "12:00 AM - 2:00 AM", "2-4": "2:00 AM - 4:00 AM", "4-6": "4:00 AM - 6:00 AM"}} input={preferences} setInput={setPreferences} />
          <Select placeholder="What time do you usually wake up?" options={{"6-8": "6:00 AM - 8:00 AM", "8-10": "8:00 AM - 10:00 AM", "10-12": "10:00 AM - 12:00 PM", "12-2": "12:00 PM - 2:00 PM"}} input={preferences} setInput={setPreferences} />
        </div>
        <div className="flex flex-col width-full justify-between gap-4 md:flex-row">
          <Select placeholder="Visitor preferences" options={{"rarely": "Rarely have visitors", "occasionally": "Occasionally have visitors", "neutral": "Neutral (comfortable with moderate visitor traffic)", "frequently": "Frequently have visitors", "always": "Always have visitors"}} input={preferences} setInput={setPreferences} />
          <Select placeholder="Cleaning habits" options={{"extremely": "Extremely neat and organized", "generally": "Generally tidy, but not overly strict", "somewhat": "Somewhat tidy, but can be messy at times", "not": "Not particularly tidy or organized"}} input={preferences} setInput={setPreferences} />
        </div>
        <button type="submit" className="border-2 border-black text-black self-center w-auto pl-5 pr-5 pt-1 pb-1 mt-8 rounded hover:bg-black hover:text-white hover:transition-colors">Submit</button>
      </form>
    </div>
  )
}

const Input = ({placeholder, name, input, setInput}: {placeholder: string, name: string, input: object, setInput: Function}) => {
  return (
    <input name={name} type="text" placeholder={placeholder} className="border-2 border-solid border-black rounded p-2 w-full placeholder-black" onChange={(e) => setInput({...input, [name]: e.target.value})} />
  )
}

const Select = ({options, placeholder, input, setInput}: {options: object, placeholder: string, input: object, setInput: Function}) => {
  return (
    <select className="border-2 border-solid border-black rounded pt-2 pb-2 pl-1 pr-1 text-black first-child:text-gray-400 w-full" defaultValue="" onChange={(e) => setInput({...input, [placeholder]: e.target.value})}>
      <option value="" className="text-gray-400" disabled hidden>{placeholder}</option>
      {Object.entries(options).map((k) => {
        return (
          <option value={k[0]} key={k[0]} className="rounded-none text-black">{k[1]}</option>
        )
      })}
    </select>
  )
}

const onSubmit = async (e: FormEvent<HTMLFormElement>, preferences: object) => {
  e.preventDefault();
  const res = await fetch('/api',  {
    method: 'POST',
    body: JSON.stringify(preferences)
  })
  if (res.status == 200) toast.success("Preferences saved!")
  else toast.error("Something went wrong!")
}