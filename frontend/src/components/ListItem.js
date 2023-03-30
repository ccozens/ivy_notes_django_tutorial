import React from 'react';
import { Link } from 'react-router-dom';

const getTitle = (note) => {
	//  split at new line and return first line as title
	const title = note.body.split('\n')[0];
	//  trim title is more than 45 characters
	if (title.length > 45) return title.substring(0, 20) + '...';
	return title;
};

const getDate = (note) => {
	const date = new Date(note.updated);
	return date.toLocaleDateString('en-GB', {
		year: 'numeric',
		month: 'short',
		day: 'numeric',
	});
};

const getContent = (note) => {
	// remove first line and return rest as content
	const content = note.body.split('\n').slice(1).join('\n');
	// trim content if more than 100 characters
	if (content.length > 45) return content.substring(0, 45) + '...';
	return content;
};

function ListItem({ note }) {
	return (
		<Link to={`/note/${note.id}`}>
			<div className="notes-list-item">
				<h3>{getTitle(note)}</h3>
				<p>
					<span>{getDate(note)}</span>
					{getContent(note)}
				</p>
			</div>
		</Link>
	);
}

export default ListItem;
