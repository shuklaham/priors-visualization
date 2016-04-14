module.exports = {

	entry:'./main.js',
	output: {
		path:'./',
		filename: 'index.js'
	},
	devServer: {
		inline: true,
		port: 3333
	},
	resolve: {
		extensions: ['', '.js', '.jsx', '.css', '.scss', '.json']
	},
	module: {
		loaders: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				loader: 'babel',
				query: {
					presets: ['es2015', 'react']
				}
			}
		]
	}
}