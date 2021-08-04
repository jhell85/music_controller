import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";

import CreateRoom from "./CreateRoom";
import JoinRoom from "./JoinRoom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/">
            <h1>home page</h1>
          </Route>
          <Route path="/join" component={JoinRoom} />
          <Route path="/create" component={CreateRoom} />
        </Switch>
      </Router>
    );
  }
}
