import React from 'react';
import WeUI from 'react-weui';

import {Dialog, Button} from 'react-weui';
const {Alert, Confirm} = Dialog;

export default class DialogTest extends React.Component{
	state = {
		buttons: [
                {
                    label: '好的',
                    onClick: this.hideConfirm.bind(this)
                }
        ],
        showConfirm:true
	};

	render(){
		return(
			<Alert  show={this.state.showConfirm}
                    title="sb" 
                    buttons={this.state.buttons}>
                警告
			</Alert>
		)
	}

	hideConfirm() {
        this.setState({showConfirm: false});
    }
}