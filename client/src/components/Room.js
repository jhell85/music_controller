import React, { Component } from "react";

export default class Room extends Component {
  constructor(props) {
    super(props);
    this.state = {
      votesToSkip: 2,
      guestCanPause: false,
      isHost: false,
    };
    this.roomCode = this.props.match.params.roomCode; // match is a prop added by ReactRouter that stores all info about how we got to this component
    this.getRoomDetails();
  }

  getRoomDetails() {
    fetch("/api/get-room" + "?code=" + this.roomCode)
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          votesToSkip: data.votes_to_skip,
          guestCanPause: data.guest_can_pause,
          isHost: data.is_host,
        });
      });
  }

  render() {
    return (
      <div>
        <h3>{this.roomCode}</h3>
        <p>Votes to skip: {this.state.votesToSkip}</p>
        <p>guest can pause: {this.state.guestCanPause.toString()}</p>
        <p>is Host: {this.state.isHost.toString()}</p>
      </div>
    );
  }
}
