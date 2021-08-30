var express = require('express');
var router = express.Router();

const { MongoClient } = require('mongodb');
const uri = 'mongodb://localhost:20170';

const client = new MongoClient(uri);


/* GET all data route */
router.get('/', async function(req, res, next) {
    let fetchedData = await allLevels();
    res.send(fetchedData);
});

/* GET Specific Level */
router.get('/:level', async function(req, res, next) {
    let fetchedData = await getSpecificLevel(parseInt(req.params.level));
    res.json(fetchedData);
});

/* GET Specific Lesson */
router.get('/:level/:lesson', async function(req, res, next) {
    let fetchedData = await getSpecificLesson(parseInt(req.params.level), parseInt(req.params.lesson));
    res.send(fetchedData);
});





// Database Functions


// Function to retrive all lesson and level data
async function allLevels() {
    await client.connect()
    const database = client.db('ttmik');
    const levels = database.collection('levels');

    const level1 = await levels.findOne({level: 2})
    await client.close()
    return level1;
}

// Function to retrive specific level
async function getSpecificLevel(chosenLevel) {
    await client.connect()
    const database = client.db('ttmik');
    const levels = database.collection('levels');

    const selectedLevel = await levels.findOne({level: chosenLevel});
    await client.close();
    return selectedLevel;
}

// Function to retrieve a specific level and lesson
async function getSpecificLesson(chosenLevel, lesson) {
    await client.connect()
    const database = client.db('ttmik');
    const levels = database.collection('levels');

    const selectedLevel = await levels.findOne({level: chosenLevel});
    await client.close();

    let lessons = Object.entries(selectedLevel.lessons)

    return lessons[lesson - 1];
}

module.exports = router;