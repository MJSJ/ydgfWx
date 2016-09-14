import React from 'react';
import WeUI from 'react-weui';

const {
 	Button,
 	Grids,
 	    Panel,
    PanelHeader,
    PanelBody,
    PanelFooter,
} = WeUI;
import {

    MediaBox,
    MediaBoxHeader,
    MediaBoxBody,
    MediaBoxTitle,
    MediaBoxDescription,
    MediaBoxInfo,
    MediaBoxInfoMeta,
    Cells,
    Cell,
    CellHeader,
    CellBody,
    CellFooter
} from 'react-weui';
import Page from "../tools/page.js"



class LA extends React.Component {

    constructor(props) {
        super(props);
        this.displayName = '';
    }
    render() {

        return (
    	<div>
    		<label>name</label>
            <input value={window.user.nickname}/>
        </div>
        );
    }
}





export default class Home extends React.Component {
	// renderItem(){
	// 	// return (

	// 	// )
	// },
  
  	render(){
  		return(
		    <Page className="home" title="WeUI" subTitle="为微信Web服务量身设计">
                <h1>welcome:</h1>
                <LA />

            </Page>
  		)
  	}
};


