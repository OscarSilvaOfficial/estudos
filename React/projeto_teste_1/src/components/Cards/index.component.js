import './style.module.css'

export const Card = (props) => {
  return (
    <li key={ props.id }>
      <h2>{ props.id }</h2>
      <p>{ props.text }</p>
      <button>Read more</button>
    </li>
  )
}