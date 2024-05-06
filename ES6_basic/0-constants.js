// enables function to be imported
export function taskFirst() {
  // declares a immutable variable
	const task = 'I prefer const when I can.';
	return task;
}

export function getLast() {
	return ' is okay';
}

export function taskNext() {
	// declares a mutable variable
	let combination = 'But sometimes let';
	combination += getLast();

	return combination;
}