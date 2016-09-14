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
    		<label>{this.props.kk}</label>
            <input value={this.props.vv}/>
        </div>
        );
    }
}
// window.user = {id: '1',gold: '0',score: '0',nickname: 'zyf',province: '北京',city: '海淀',country: '中国'}




export default class Home extends React.Component {
	renderItem(){
		var user = window.user;
		var results = [];

		for(let i in user){
			results.push (<LA kk={i} vv={user[i]} key={i}></LA>);
		
		}
		return results;
	}
  
  	render(){
  		return(
		    <Page className="home" title="WeUI" subTitle="为微信Web服务量身设计">
                <h1>welcome:</h1>
              		{this.renderItem()}
		
            </Page>
  		)
  	}
};


