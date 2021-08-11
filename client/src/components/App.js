import React, { Component } from "react";
import { render } from "react-dom";
import { Container } from "@material-ui/core";

import HomePage from "./HomePage";

export default class App extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <Container>
        <HomePage />
      </Container>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
