import { useState } from 'react'
//import reactLogo from 'assets/react.svg'
//import viteLogo from '/vite.svg'
import '../../App.css'
import DetailSpan from 'components/Span/DetailSpan'
//import Database from 'api/Database'
/*const Demo = (
  <>
    <div>
      <a href="https://vitejs.dev" target="_blank">
        <img src={viteLogo} className="logo" alt="Vite logo" />
      </a>
      <a href="https://react.dev" target="_blank">
        <img src={reactLogo} className="logo react" alt="React logo" />
      </a>
    </div>
    <h1>Vite + React</h1>
    <div className="card">
      <button onClick={() => setCount((count) => count + 1)}>
        count is {count}
      </button>
      <p>
        Edit <code>src/App.jsx</code> and save to test HMR
      </p>
    </div>
    <p className="read-the-docs">
      Click on the Vite and React logos to learn more
    </p>
  </>
)
*/

const info = {
  title: "Bienvenido a PYG4",
  article: "En esta pagina te ayudaremos a desarrollar el curso " +
    "de Arquitectura de Computadoras de una forma interactiva "+ "con el fin de facilitarte la comprencion y el desarrollo del curso"+
    "con tu asistente virtual de esta manera no tienes la nesecidad de leer completamente la informacion conrrespondiente"+
    "Nuestro asistente lo hara por usted, as como proporcionarle imagenes relevantes para una mayor comprencion "+"",
  intro: "Bienvenido al curso de arquitectura de computadoras, donde aprenderas los principios y conceptos basicos que" +
    "rigen el diseño y funcionamiento de los sistemas informaticos. Mi nombre es PYG-4 y estoy aqui para "+
    "ayudarte en tu proceso de aprendizaje",
  sections: [
    {
      side: "left",
      icon: "",
      title: "Demo",
      href:"/demo",
      content: "En este apartado tenemos tres posibles opciones \n"+
      "Aprender: En este apartado podras interactuar con nuestro asistente virtual PYG-4 en el cual podras aventurarte en los distintos"+
      "temas que te brindamos\n"+
      "Quiz: Aqui podras poner a prueba tus conocimientos adquiridos usando el asistente virtual\n"+
      "Juegos: Aqui podras ampliar tus conceptos interactuando con nuestros juegos ",
    },
    {
      side: "right",
      icon: "",
      title: "Desarrollar",
      href:"/dev",
      content: "En este apartado esata por verse",
    },
    {
      side: "left",
      icon: "",
      href: "/about",
      title: "Mas informacion",
      content: "esta por verse ",
    },
    {
      side: "right",
      icon: "",
      href: "/download",
      title: "Descargar App",
      content: "Aqui podras hacerte con tu propio asistente virtual sin nesecidad de estar con la red",
    }
    
  ],
}

function Index() {
  const [count, setCount] = useState(0) 
  
  return (
    <div className="flex flex-col font-mono items-center w-full py-4">
      <h1 className="text-6xl  m-10"> {info.title} </h1> 
      <p className="text-lg text-center w-3/4 m-5"> {info.intro} </p>
      <article className="text-lg text-justify w-3/4 m-5 bg-gray-600 p-4 rounded-md">
        {info.article}
      </article>
      {info.sections.map((e,i) => (
        <DetailSpan key={i} data={e} />
      ))}
    </div>
  )
}

export default Index
