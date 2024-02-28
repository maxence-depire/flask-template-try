let n = 0;
const container = document.getElementById("app")

function render() {
    const title = React.createElement('h1', {},
        'Hello World ! ',
        React.createElement('span', {}, n)
    )

    ReactDOM.render(title, container)
}

render()

window.setInterval(() => {
    n++
    render()
}, 1000)