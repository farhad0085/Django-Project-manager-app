import React from 'react';


const CardItem = ({ item }) => {

    return (
        <li className="list-group-item">
            {item.title}
        </li>
    )
}


const ProjectDetail = ({ card }) => {

    return (
        <div className="col-md-12 col-xl-4">
            <div className="card p-4">
                <h3>{card.title}</h3>
                <p className="text-muted">{card.description}</p>
                <hr />
                <ul className="list-group">
                    {card.carditem_set.map(item => <CardItem item={item} />)}
                </ul>
            </div>
        </div>
    )

}

export default ProjectDetail;