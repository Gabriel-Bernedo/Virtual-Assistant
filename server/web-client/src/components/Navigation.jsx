
import { Link } from 'react-router-dom'

export default function Navigation() {
  return (
    <header className="masthead mb-auto">
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <Link to="/demo/" className="navbar-brand">SciSync</Link>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="nav nav-pills">
                    <li className="nav-item active">
                        <Link to="/home/" className="nav-link"> Inicio <span className="sr-only">(current)</span> </Link>
                    </li>
                    <li className="nav-item">
                        <Link to="/features/" className="nav-link"> Detalles </Link>
                    </li>
                    <li className="nav-item">
                        <Link to="/docs/" className="nav-link"> Documentacion </Link>
                    </li>
                    <li className="nav-item">
                        <Link to="#" className="nav-link disabled"> Disabled </Link>
                    </li>
                    <li>
                        <Link to="/questions/" className="nav-link active"> Cuestionario </Link>
                    </li>
                </ul>
            </div>
        </nav>
    </header>
  )
}
