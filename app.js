// third party imports
const express = require("express");
const helmet = require("helmet");
const cors = require("cors");
const morgan = require("morgan");

require("dotenv").config();

// local imports
const downloadRouter = require("./controllers/download");

const app = express();

// middleware
app.use(helmet());
app.use(cors());
app.use(morgan("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// routes
app.use("/api/download", downloadRouter);

// endpoints

module.exports = app;
