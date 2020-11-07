import React from 'react';


const CardItem = ({ item }) => {

    return (
        <li className="list-group-item">
            {item.title}
        </li>
    )
}


const Card = ({ card }) => {

    return (
        <div className="col-md-12 col-xl-4">
            <div className="card p-4 shadow-nohover">
                <h3>{card.title}</h3>
                <p className="text-muted mb-0">{card.description}</p>
                <hr />
                <ul className="list-group">
                    {card.carditem_set.map(item => <CardItem item={item} />)}
                    {!card.carditem_set.length && "No item here"}
                </ul>
            </div>
        </div>
    )

}

export default Card;