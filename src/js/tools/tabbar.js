import React from 'react';
import classNames from 'classnames';
import WeUI from 'react-weui';

const {
 	TabBarIcon,
 	TabBarLabel
} = WeUI;


export default class TabBarItem extends React.Component {
    static propTypes = {
      active: React.PropTypes.bool,
      icon: React.PropTypes.any,
      label: React.PropTypes.string
    };

    static defaultProps = {
      active: false,
      icon: false,
      label: ''
    };

    render() {

        const {children, className, active, icon, label,href, ...others} = this.props;
        const cls = classNames({
            weui_tabbar_item: true,
            weui_bar_item_on: active
        }, className);

        if(icon || label){
            return (
                <a href={href} className={cls} {...others}>
                    {icon ? <TabBarIcon>{icon}</TabBarIcon> : false}
                    {label ? <TabBarLabel>{label}</TabBarLabel> : false}
                </a>
            )
        }else{
            return (
                <a href={href} className={cls} {...others}>
                    {children}
                </a>
            );
        }
    }
}