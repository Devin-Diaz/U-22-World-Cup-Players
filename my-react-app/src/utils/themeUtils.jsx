// src/utils/themeUtils.js

export function getPlayerTheme(player) {

    // Grab the three most dominant flag colors
    const colors = [...player.flag_colors]
        .sort((a, b) => b.percent - a.percent)
        .slice(0, 3);

    // Convert "#RRGGBB" -> "#RRGGBBAA"
    function withAlpha(hex, alpha) {

        const alphaHex = Math.round(alpha * 255)
            .toString(16)
            .padStart(2, "0")
            .toUpperCase();

        return `${hex}${alphaHex}`;
    }

    // Determine how transparent a color should be
    // Bright colors become more transparent so they don't overwhelm the card.
    function getAlpha(hex) {

        const r = parseInt(hex.slice(1, 3), 16);
        const g = parseInt(hex.slice(3, 5), 16);
        const b = parseInt(hex.slice(5, 7), 16);

        const brightness =
            0.299 * r +
            0.587 * g +
            0.114 * b;

        if (brightness > 220) return 0.12; // White
        if (brightness > 170) return 0.18; // Light colors
        if (brightness > 100) return 0.25; // Medium colors
        return 0.35;                       // Dark colors
    }

    const gradient = `linear-gradient(
        135deg,
        ${colors
            .map(color => withAlpha(color.hex, getAlpha(color.hex)))
            .join(", ")}
    )`;

    return {
        gradient,
        border: colors[0].hex,
        primary: colors[0].hex,
        secondary: colors[1]?.hex ?? colors[0].hex,
        accent: colors[2]?.hex ?? colors[0].hex
    };
}