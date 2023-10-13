
import { Link } from 'react-router-dom'

export default function Navigation() {
  return (
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <Link to="/demo/" className="navbar-brand">SciSync</Link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
            <li class="nav-item active">
                <Link to="/home/" className="nav-link"> Inicio <span class="sr-only">(current)</span> </Link>
            </li>
            <li class="nav-item">
                <Link to="/features/" className="nav-link"> Detalles </Link>
            </li>
            <li class="nav-item">
                <Link to="/docs/" className="nav-link"> Documentacion </Link>
            </li>
            <li class="nav-item">
                <Link to="#" className="nav-link disabled">Disabled</Link>
                <a class="nav-link disabled" href="#">Disabled</a>
            </li>
            </ul>
        </div>
    </nav>
  )
}
