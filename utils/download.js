const axios = require("axios");
class Download {
  constructor(id) {
    this.id = id;
    this.axios = axios;
  }

  // download what files specified in the id
  async download() {
    try {
      const formatedUrl = this.getFormaterdUrl(this.id);
      const response = await this.getResponseBack(formatedUrl);
      console.log(response.data);
      const type = this.getType(response);

      if (type == "image") {
        return this.download_image(response);
      } else if (type == "video") {
        return this.download_video(response);
      } else {
        return {
          msg: "Please, check the id",
        };
      }
    } catch (e) {
      console.log(e);
      return {
        msg: "Error while downloading",
        error: e,
      };
    }
  }

  async getResponseBack(url) {
    const response = await this.axios.get(url);
    return response;
  }

  getFormaterdUrl(id) {
    return "https://www.instagram.com/p/" + id + "?__a=1";
  }

  getType(response) {
    const type =
      response.data.graphql.shortcode_media.__typename == "GraphVideo"
        ? "video"
        : "image";

    if (type != "image" && type != "video") {
      return false;
    }
    return type;
  }

  async download_image(res) {
    // get actual url
    const url = res.data.graphql.shortcode_media.display_url;
    const file = await this.axios.get(url, { responseType: "stream" });
    const fileName = "instagram_" + Date.now() + ".png";
    const filePath = `./${fileName}`;
    file.data.pipe(fs.createWriteStream(filePath));

    return {
      msg: "Downloading Image",
      imagePath: filePath,
    };
  }

  async download_video(res) {
    console.log("Video");
    return {
      msg: "Downloading Video",
      res: res,
    };
  }
}

module.exports = Download;
