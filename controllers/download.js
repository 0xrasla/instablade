const downloadRouter = require("express").Router();
const Download = require("../utils/download");

downloadRouter.get("/:id", (req, res) => {
  const { id } = req.params;
  const download = new Download(id);
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
