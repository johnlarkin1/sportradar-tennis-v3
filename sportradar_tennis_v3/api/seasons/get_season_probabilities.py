from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_season_probabilities_locale import GetSeasonProbabilitiesLocale
from ...models.get_season_probabilities_response_200 import GetSeasonProbabilitiesResponse200
from ...types import Response


def _get_kwargs(
    locale: GetSeasonProbabilitiesLocale,
    urn_season: str,
    format: str = "json",  # Added format parameter with default "json"
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/seasons/{urn_season}/probabilities" + f".{format}",  # Append format to URL
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetSeasonProbabilitiesResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetSeasonProbabilitiesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetSeasonProbabilitiesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetSeasonProbabilitiesLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetSeasonProbabilitiesResponse200]:
    """show probabilities for all sport events in a season

     Show a probabilities for all sport events in a season.

    Args:
        locale (GetSeasonProbabilitiesLocale):
        urn_season (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSeasonProbabilitiesResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_season=urn_season, format=format)

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: GetSeasonProbabilitiesLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to shorthand function as well
) -> Optional[GetSeasonProbabilitiesResponse200]:
    """show probabilities for all sport events in a season

     Show a probabilities for all sport events in a season.

    Args:
        locale (GetSeasonProbabilitiesLocale):
        urn_season (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSeasonProbabilitiesResponse200
    """

    return sync_detailed(
        locale=locale,
        urn_season=urn_season,
        client=client,
        format=format,  # Pass format to sync_detailed
    ).parsed


async def asyncio_detailed(
    locale: GetSeasonProbabilitiesLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetSeasonProbabilitiesResponse200]:
    """show probabilities for all sport events in a season

     Show a probabilities for all sport events in a season.

    Args:
        locale (GetSeasonProbabilitiesLocale):
        urn_season (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSeasonProbabilitiesResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_season=urn_season, format=format)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: GetSeasonProbabilitiesLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to async shorthand function
) -> Optional[GetSeasonProbabilitiesResponse200]:
    """show probabilities for all sport events in a season

     Show a probabilities for all sport events in a season.

    Args:
        locale (GetSeasonProbabilitiesLocale):
        urn_season (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSeasonProbabilitiesResponse200
    """

    return (
        await asyncio_detailed(
            locale=locale,
            urn_season=urn_season,
            client=client,
            format=format,  # Pass format to asyncio_detailed
        )
    ).parsed
