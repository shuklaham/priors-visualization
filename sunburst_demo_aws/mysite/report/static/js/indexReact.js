

//var jsonObject = JSON.parse('{{ band | escapejs }}');

var CommentBox = React.createClass({
  render: function() {
    return (
      <div className="commentBox">
        <img src='/static/images/cube.gif' />
        Hello, world! I am a CommentBox.
      </div>
    );
  }
});
ReactDOM.render(
  <CommentBox />,
  document.getElementById('content')
);