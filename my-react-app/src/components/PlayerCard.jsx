import '../css/PlayerCard.css'
import { getPlayerTheme } from '../utils/themeUtils';

// Renders a player's details


function PlayerCard({player}) {
    const theme = getPlayerTheme(player)
    console.log(theme)
    return (
        <article className="player-card"
            style={{
                background: theme.gradient,
                border: `3px solid ${theme.border}`
            }}
        >
        
            <img
                src={player.player_image_url}
                alt={player.player_name}
                style={{
                    width: "100%",
                    height: "180px",
                    objectFit: "contain"
                }}
            />

            <h2 className="player-name">{player.name_on_shirt}</h2>
            <p>{player.pos } - #{player.jersey_num}</p>
            <p>{player.country} ({player.country_code})</p>
            
            <img
                src={player.flag_url}
                alt={`${player.country} flag`}
                width="40"
            />

            <p className="player-club">{player.club}</p>

            <p>Caps: {player.caps} - Goals: {player.goals}</p>

        </article>
    )

}

export default PlayerCard