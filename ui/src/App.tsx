import { useState } from 'react';
import './App.css'


import URLShortener from './components/UrlShortener';
import Header from './components/Header';

function App() {
  return (
    <> 
      <Header />
      <URLShortener />
    </>
  );
}

export default App;