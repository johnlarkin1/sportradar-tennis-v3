from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_season_standings_locale import GetSeasonStandingsLocale
from ...types import UNSET, Response, Unset


def _get_kwargs(
    locale: GetSeasonStandingsLocale,
    urn_season: str,
    *,
    round_: Union[Unset, int] = 0,
    live: Union[Unset, bool] = True,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["round"] = round_

    params["live"] = live

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/seasons/{urn_season}/standings",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
) -> Response[Any]:
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
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
        urn_season=urn_season,
        round_=round_,
        live=live,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    locale: GetSeasonStandingsLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    round_: Union[Unset, int] = 0,
    live: Union[Unset, bool] = True,
) -> Response[Any]:
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
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
        urn_season=urn_season,
        round_=round_,
        live=live,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
