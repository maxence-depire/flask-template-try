let n = 0;
const container = document.getElementById("app")

function render() {
    const title = React.createElement('h1', {},
        'Hello World ! '
    )

    ReactDOM.render(title, container)
}

render()