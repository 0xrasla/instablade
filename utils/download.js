const axios = require("axios");

//https%3A%2F%2Fwww.instagram.com%2Fp%2FCeT3oxNM7N0%2F%3Futm_source%3Dig_web_copy_link

class Download {
  constructor(url) {
    this.url = url;
    this.axios = axios;
  }

  // download what files specified in the url
  async download() {
    const formatedUrl = this.getFormaterdUrl(this.url);
    const response = await this.getResponseBack(formatedUrl);
    const type = this.getType(response);

    if (type == "image") {
      this.download_image();
    } else if (type == "video") {
      this.download_video();
    } else {
      console.log("Invalid url");
    }
  }

  async getResponseBack(url) {
    const niceUrl = this.getFormaterdUrl(url);
    const response = await this.axios.get(niceUrl);
    return response;
  }

  getFormaterdUrl(url) {
    return url + "?__a=1";
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
    return {
      msg: "Downloading Image",
      res: res,
    };
  }

  async download_video(res) {
    return {
      msg: "Downloading Video",
      res: res,
    };
  }
}

module.exports = Download;
