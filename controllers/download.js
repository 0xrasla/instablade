const downloadRouter = require("express").Router();
const Download = require("../utils/download");

downloadRouter.get("/", (req, res) => {
  const { url } = req.query;
  const download = new Download(url);
  download
    .download()
    .then((response) => {
      res.status(200).json(response);
    })
    .catch((e) => {
      res.status(500).json({
        msg: "Error while downloading",
      });
    });
});

module.exports = downloadRouter;
