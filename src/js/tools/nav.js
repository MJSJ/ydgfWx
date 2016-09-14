import React from 'react';
import { Router, Route, IndexRoute ,browserHistory,hashHistory} from 'react-router';


import WeUI from 'react-weui';

const {
 	Button,
 	Grids,
 	Tab,
 	TabBar
} = WeUI;

import TabBarItem from "../tools/tabbar.js"
import Page from "../tools/page.js"

import IconButton from '../../img/icon_nav_button.png';
import IconCell from '../../img/icon_nav_cell.png';
import IconToast from '../../img/icon_nav_toast.png';
import IconDialog from '../../img/icon_nav_dialog.png';
import IconProgress from '../../img/icon_nav_progress.png';
import IconMsg from '../../img/icon_nav_msg.png';
import IconArticle from '../../img/icon_nav_article.png';
import IconActionSheet from '../../img/icon_nav_actionSheet.png';
import IconIcons from '../../img/icon_nav_icons.png';
import IconPanel from '../../img/icon_nav_panel.png';
import IconTab from '../../img/icon_nav_tab.png';
import IconSearchBar from '../../img/icon_nav_search_bar.png';


export default class Nav extends React.Component {
  	state = {
        components: [{
            icon: IconButton,
            label: 'Buton',
            href: '#/button',
            index: 0
        }, {
            icon: IconCell,
            label: 'Cell',
            href: '#/cell',
            index: 1
        }, {
            icon: IconToast,
            label: 'home',
            href: '#/home',
            index: 2
        }, {
            icon: IconDialog,
            label: 'Dialog',
            href: '#/dialog',
            index: 3
        }
        ]
    };


    renderItem(){
        return this.state.components.map((v,k)=>{
            return (
                <TabBarItem icon={<img src={v.icon}/>} key={`tab_item_${k}`} label={v.label} href={v.href}
                active={this.state.tab == k} onClick={e=>this.setState({tab:k})} /> 
            );
        });
    }
  	render(){
  		var tabItems = this.renderItem();
  		return(
  
		   		<TabBar>
                   {tabItems}
                </TabBar>
     
  		)
  	}
};
