import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Link } from 'react-router-dom';
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg';

function NotePage(props) {
	// get id from url
	const { noteId } = useParams();
	const [note, setNote] = useState(null);

	// get note by id
	useEffect(() => {
		getNote();
	}, [noteId]);

	const getNote = async () => {
		//  don't trigger getNote if noteId is new
		if (noteId === 'new') return;
		//  otherwise, do
		const response = await fetch(
			`http://localhost:8000/api/notes/${noteId}`
		);
		const data = await response.json();
		setNote(data);
	};

	// create note
	const createNote = async () => {
		await fetch(`http://localhost:8000/api/notes/create/`, {
			method: 'POST',
			headers: {
				'Content-type': 'application/json',
			},
			// body: JSON.stringify({ ...note, updated: new Date() }),
			body: JSON.stringify(note),
		});
	};

	// update note
	const updateNote = async () => {
		// await fetch(`http://localhost:8000/notes/${noteId}`, {
		await fetch(`http://localhost:8000/api/notes/${noteId}/update/`, {
			method: 'PUT',
			headers: {
				'Content-type': 'application/json',
			},
			// usually body: JSON.stringify(note) is enough and backend handles update, but json-server needs this
			// body: JSON.stringify({ ...note, updated: new Date() }),
			body: JSON.stringify(note),
		});
	};

	const deleteNote = async () => {
		await fetch(`http://localhost:8000/api/notes/${noteId}/delete/`, {
			method: 'DELETE',
			headers: {
				'Content-type': 'application/json',
			},
		});
	};

	const handleSubmit = (e) => {
		// if noteId is not new and note body is empty, delete it
		if (noteId !== 'new' && !note.body) {
			deleteNote();
		}
		// if noteId is not new and note.body has content, update note
		else if (noteId !== 'new' && note.body) {
			updateNote();
		}
		// if noteId is new and body has content, create note
		else if (noteId === 'new' && note.body) {
			createNote();
		}
	};

	return (
		<div className="note">
			<div className="note-header">
				<h3>
					<Link to="/">
						<ArrowLeft onClick={handleSubmit} />
					</Link>
				</h3>
				{noteId !== 'new' ? (
					<Link to="/">
						<button onClick={deleteNote}>Delete</button>
					</Link>
				) : (
					<Link to="/">
						<button onClick={handleSubmit}>Done</button>
					</Link>
				)}
			</div>
			<textarea
				value={note ? note.body : ''}
				onChange={(e) => {
					setNote({ ...note, body: e.target.value });
				}}></textarea>
		</div>
	);
}

export default NotePage;
