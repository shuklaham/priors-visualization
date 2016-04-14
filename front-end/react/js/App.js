import React from 'react';
import ReactDom from 'react-dom' ;
import Chart from './chart';


class App extends React.Component{
	componentWillMount() {
		//API call here
	}

	render() {
		return (
			<div>
				<p className="header">Sunburst</p>
				<div>
					<p className="info">Patient Name: <span className="span">Praveen</span></p>
					<p className='info'>Patient MRN: <span className="span">Abc</span></p>
					<p className='info'>Exam Type: <span className="span">CTScan</span></p>
				</div>
				<Chart/>
			</div>
		);
	}
}

ReactDom.render(<App/>, document.getElementById('app'))