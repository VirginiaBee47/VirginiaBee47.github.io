/*
Author: Virginia Covert
Created: 23-06-2025
Title: scrab.js
Description: This script is an emulator for scrabble in javascript for server
    hosting. It interfaces with scrab.html and scrab.css to create a simple 
    scrabble game.
*/

/*
import { DatabaseSync } from 'http://node:sqlite';

const database = new DatabaseSync('./db.sqlite');

database.exec(`
    CREATE TABLE IF NOT EXISTS board(
        id INTEGER PRIMARY KEY,
        row INTEGER,
        col INTEGER,
        letter TEXT,
        isBlank BOOLEAN,
        player TEXT,
        turnPlayed INTEGER
    ) STRICT
    CREATE TABLE IF NOT EXISTS players(
        playerId INTEGER PRIMARY KEY,
        name TEXT,
        score INTEGER,
        isTurn BOOLEAN,
        tiles TEXT
    )
`);

const insertTile = database.prepare(`
    INSERT INTO board (row, col, letter, isBlank, player, turnPlayed) VALUES (?, ?, ?, ?, ?, ?)
`);

const initPlayer = database.prepare(`
    INSERT INTO players (name, tiles) VALUES (?, ?)
`);

const updatePlayer = database.prepare(`
    UPDATE players SET score = ?, isTurn = ?, tiles = ? WHERE name = ?
`);

const getBoard = database.prepare(`
    SELECT row, col, letter, isBlank, player, turnPlayed FROM board
`);
*/

function startGame() {
    console.log("Game started!");
    let tiles = [];
    for (let i = 0; i < 7; i++) {
        tiles.push('A'); 
    }
    document.getElementById('letters').innerHTML = tiles.join(', ');
    document.getElementById('score').innerHTML = "0";
}

document.getElementById('startGame').addEventListener('click', startGame);