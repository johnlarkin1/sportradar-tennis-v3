from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_season_standings_locale import GetSeasonStandingsLocale
from ...models.get_season_standings_response_200 import GetSeasonStandingsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    locale: GetSeasonStandingsLocale,
    urn_season: str,
    *,
    round_: Union[Unset, int] = 0,
    live: Union[Unset, bool] = True,
    format: str = "json",  # Added format parameter with default "json"
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["round"] = round_

    params["live"] = live

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/seasons/{urn_season}/standings" + f".{format}",  # Append format to URL
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetSeasonStandingsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetSeasonStandingsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetSeasonStandingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetSeasonStandingsLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    round_: Union[Unset, int] = 0,
    live: Union[Unset, bool] = True,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetSeasonStandingsResponse200]:
    """get the standings for a season

     Get the standings for a season.

    Args:
        locale (GetSeasonStandingsLocale):
        urn_season (str):
        round_ (Union[Unset, int]):  Default: 0.
        live (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSeasonStandingsResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_season=urn_season, round_=round_, live=live, format=format)

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: GetSeasonStandingsLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    round_: Union[Unset, int] = 0,
    live: Union[Unset, bool] = True,
    format: str = "json",  # Added format parameter to shorthand function as well
) -> Optional[GetSeasonStandingsResponse200]:
    """get the standings for a season

     Get the standings for a season.

    Args:
        locale (GetSeasonStandingsLocale):
        urn_season (str):
        round_ (Union[Unset, int]):  Default: 0.
        live (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSeasonStandingsResponse200
    """

    return sync_detailed(
        locale=locale,
        urn_season=urn_season,
        client=client,
        round_=round_,
        live=live,
        format=format,  # Pass format to sync_detailed
    ).parsed


async def asyncio_detailed(
    locale: GetSeasonStandingsLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    round_: Union[Unset, int] = 0,
    live: Union[Unset, bool] = True,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetSeasonStandingsResponse200]:
    """get the standings for a season

     Get the standings for a season.

    Args:
        locale (GetSeasonStandingsLocale):
        urn_season (str):
        round_ (Union[Unset, int]):  Default: 0.
        live (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSeasonStandingsResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_season=urn_season, round_=round_, live=live, format=format)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: GetSeasonStandingsLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    round_: Union[Unset, int] = 0,
    live: Union[Unset, bool] = True,
    format: str = "json",  # Added format parameter to async shorthand function
) -> Optional[GetSeasonStandingsResponse200]:
    """get the standings for a season

     Get the standings for a season.

    Args:
        locale (GetSeasonStandingsLocale):
        urn_season (str):
        round_ (Union[Unset, int]):  Default: 0.
        live (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSeasonStandingsResponse200
    """

    return (
        await asyncio_detailed(
            locale=locale,
            urn_season=urn_season,
            client=client,
            round_=round_,
            live=live,
            format=format,  # Pass format to asyncio_detailed
        )
    ).parsed
