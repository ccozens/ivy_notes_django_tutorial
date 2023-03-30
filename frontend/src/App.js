import './App.css';
import Header from './components/Header';
import NotesListPage from './pages/NotesListPage';
import Footer from './components/Footer';
import NotePage from './pages/NotePage';
import {
	BrowserRouter as Router,
	Routes,
	Route,
} from 'react-router-dom';

function App() {
	return (
		<Router>
			<div className="container dark">
        <div className="app">
          
				<Header />
				<Routes>
					<Route path="/" exact Component={NotesListPage} />
          <Route path="/note/:noteId" Component={NotePage} />
				</Routes>
				<Footer />
        </div>
			</div>
		</Router>
	);
}

export default App;
